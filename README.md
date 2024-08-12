# Based on https://github.com/jpylypiw/easywall, original repository has been moved to archive 

**Firewalls** are becoming increasingly important in today's world. Hackers and automated scripts are constantly trying to **invade your system** and use it for Bitcoin mining, botnets or other things.

To prevent these attacks, you can use a firewall on your system. **IPTables** is the strongest firewall in Linux because it can **filter packets in the kernel** before they reach the application. Using IPTables is **not very easy** for Linux beginners. We have created easywall - the simple **IPTables web interface**. The focus of the software is on easy installation and use.

![Home Screen](https://i.imgur.com/Tk1Mbvv.png)

---

## Demo

**The demo is currently not available because a new server has to be installed for this purpose.**

You can view an online version of the program as a demo under the following link:

<https://addurlhere> (Certificate is provided by Let's Encrypt)

- **Username**: demo
- **Password**: demo

The online demo version is reset every 30 minutes and all data is deleted. The demo has only the frontend installed without the backend. Configuration changes are therefore not saved or applied.

---

## Quick Start

This guide refers to the easiest way to install using the APT Package Manager. For detailed installation instructions, please refer to the [documentation](https://github.com/jpylypiw/easywall/blob/master/docs/INSTALL.md).

```sh
apt update
apt install -y apt-transport-https gnupg
echo "deb https://apt.wdkro.de/ stable main" > /etc/apt/sources.list.d/easywall.list
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 67A12A6883B73731
apt update
apt install easywall
```

After installation, the web interface can be accessed in the browser at <https://hostname-or-ip-address:12227>.

---

## Features

- **Built-in rules** - that can be activated by option.
- **Logging** - of blocked connections and many other stuff.
- **IPv6** - is completely supported since it should be used on every system.
- **Two step activation** - Changed rules are activated in two steps to check the connection.
- **Blacklisting and Whitelisting** - of IP addresses and IPv6 addresses.
- **Port Forwarding** - Forward Ports through the Firewall.
- **TCP, UDP and Port Ranges** - Open them if you need them in the internet.
- **Own IPTables rules** - Can be managed in the web interface.
- **Install and Update** - The software can be installed and updated easily.
- **Ansible role**- For advanced users and automation.

---

## Roadmap

The following features will be implemented in one of the next versions. If you need a feature, simply create a GitHub issue, and we'll include it here.

- :x: finish all `TODO: Docs` documentations
- :x: improve testing by using multiple os

---

## Install

We provide extensive instructions on our [installation](https://github.com/jpylypiw/easywall/blob/master/docs/INSTALL.md) page.
You can find a script for automatic downloading and installation.

---

## Ansible Role

We are currently working on an Ansible role that will allow easywall to be fully configured with Ansible.

The project can be found under the following link:
**[ansible-role-easywall](https://github.com/jpylypiw/ansible-role-easywall)**

---

## Documentation

Check the **[docs folder](https://github.com/jpylypiw/easywall/tree/master/docs)** for the software documentation.

---

## License

easywall is GNU General Public License v3.0 +.

---

## Support me

The project easywall was created in a time when I did not have any knowledge about Linux. Today I work as an administrator for Linux systems and would not need this project anymore. Nevertheless it is important to me to support the introduction to Linux and the use and simplification of firewalls.

To continue the project, I need your support! Please donate so that I can continue the project in my spare time. Every dollar counts! You can find a donation link on [GitHub](https://github.com/jpylypiw/easywall).

---

## What does it look like

![Screenshot 1](https://i.imgur.com/eQAHOUc.png)
![Screenshot 2](https://i.imgur.com/N2cdm0h.png)
![Screenshot 3](https://i.imgur.com/pjtJuq5.png)
![Screenshot 4](https://i.imgur.com/SSTPaXO.png)
![Screenshot 5](https://i.imgur.com/EPHUjI3.png)
![Screenshot 6](https://i.imgur.com/X3sdFO3.png)
![Screenshot 7](https://i.imgur.com/5kd2Nql.png)
![Screenshot 8](https://i.imgur.com/jjZTxrV.png)
![Screenshot 9](https://i.imgur.com/owPACSx.png)
