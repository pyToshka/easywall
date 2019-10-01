import json
import os
import platform
import time
import urllib
from datetime import datetime, timezone

from flask import session

import utility
from config import Config
from defaultpayload import DefaultPayload


class webutils(object):
    def __init__(self):
        self.cfg = Config("../config/config.ini")

    def check_login(self):
        """the function checks if the user/session is logged in"""
        if not session.get('logged_in'):
            return False
        return True

    def get_default_payload(self, title, css="easywall"):
        """the function creates a object of information that are needed on every page"""
        payload = DefaultPayload()
        payload.year = datetime.today().year
        payload.title = title
        payload.customcss = css
        payload.machine = self.get_machine_infos()
        payload.latest_version = self.cfg.get_value("VERSION", "version")
        payload.current_version = utility.file_get_contents("../.version")
        payload.commit_sha = self.cfg.get_value("VERSION", "sha")
        payload.commit_date = self.get_commit_date(self.cfg.get_value("VERSION", "date"))
        return payload

    def get_machine_infos(self):
        """the function retrieves some information about the host and returns them as a list"""
        infos = {}
        infos["Machine"] = platform.machine()
        infos["Hostname"] = platform.node()
        infos["Platform"] = platform.platform()
        infos["Python Build"] = platform.python_build()
        infos["Python Compiler"] = platform.python_compiler()
        infos["Python Implementation"] = platform.python_implementation()
        infos["Python Version"] = platform.python_version()
        infos["Release"] = platform.release()
        infos["Libc Version"] = platform.libc_ver()
        return infos

    def get_commit_date(self, datestring):
        """
        the function compares a datetime with the current date
        for comparing the datestring parameter is in UTC timezone
        """
        date1 = datetime.strptime(str(datestring), "%Y-%m-%dT%H:%M:%SZ")
        date1 = date1.replace(
            tzinfo=timezone.utc).astimezone(
                tz=None).replace(
                    tzinfo=None)
        date2 = datetime.now()
        return utility.time_duration_diff(date1, date2)

    def update_last_commit_infos(self):
        """
        the function retrieves the last commit information after a specific waiting time
        after retrieving the information they are saved into the config file
        """
        currtime = int(time.time())
        lasttime = int(self.cfg.get_value("VERSION", "timestamp"))
        waitseconds = 3600  # 60 minutes × 60 seconds
        if currtime > (lasttime + waitseconds):
            commit = self.get_latest_commit()
            self.cfg.set_value("VERSION", "version", self.get_latest_version())
            self.cfg.set_value("VERSION", "sha", commit["sha"])
            self.cfg.set_value("VERSION", "date", commit["commit"]["author"]["date"])
            self.cfg.set_value("VERSION", "timestamp", currtime)

    def get_latest_commit(self):
        """
        retrieves the informations of the last commit from github as json
        and converts the information into a python object
        for example the object contains the last commit date and the last commit sha
        This function should not be called very often, because GitHub has a rate limit implemented
        """
        url = "https://api.github.com/repos/jpylypiw/easywall/commits/master"
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'EasyWall Firewall by JPylypiw'
            }
        )
        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode('utf-8'))

    def get_latest_version(self):
        """
        the function retrieves the latest version from github and returns the version string
        """
        url = "https://raw.githubusercontent.com/jpylypiw/easywall/master/.version"
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'EasyWall Firewall by JPylypiw'
            }
        )
        response = urllib.request.urlopen(req)
        data = response.read()
        return data.decode('utf-8')

    def get_rule_list(self, ruletype):
        """
        the function reads a file into the ram and returns a list of all rows in a list
        for example you get all the ip addresses of the blacklist in a array
        """
        rule_list = []
        filepath = self.cfg.get_value(
            "RULES", "filepath") + "/" + self.cfg.get_value("RULES", ruletype)
        if filepath.startswith("."):
            filepath = "../" + filepath
        with open(filepath, 'r') as rulesfile:
            for rule in rulesfile.read().split('\n'):
                if rule.strip() != "":
                    rule_list.append(rule)
        return rule_list

    def get_last_accept_time(self):
        """
        the function retrieves the modify time of the acceptance file and compares the time to the current time
        """
        filepath = "../" + self.cfg.get_value("ACCEPTANCE", "filename")
        if os.path.exists(filepath):
            mtime = os.path.getmtime(filepath)
            mtime = datetime.utcfromtimestamp(mtime)
            mtime = mtime.replace(
                tzinfo=timezone.utc).astimezone(
                tz=None).replace(
                    tzinfo=None)
            now = datetime.now()
            return utility.time_duration_diff(mtime, now)
        else:
            return "never"

    def save_rule_list(self, ruletype, rulelist):
        """
        the function writes a list of strings into a rulesfile
        for example it saves the blacklist rules into the blacklist rulesfile
        """
        filepath = self.cfg.get_value(
            "RULES", "filepath") + "/" + self.cfg.get_value("RULES", ruletype)
        if filepath.startswith("."):
            filepath = "../" + filepath
        with open(filepath, mode='wt', encoding='utf-8') as rulesfile:
            rulesfile.write('\n'.join(rulelist))
        return True