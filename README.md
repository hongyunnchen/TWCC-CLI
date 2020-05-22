###### tags: `twcc`, `twccli`

[![CircleCI](https://circleci.com/gh/TW-NCHC/TWCC-CLI/tree/v0.5.svg?style=shield)](https://circleci.com/gh/TW-NCHC/TWCC-CLI/tree/v0.5)


# TWCC-CLI Project

The TWCC Command Line Interface (CLI) is an environment to create and manage your TWCC services. The current version of the TWCC CLI is **v0.5**. (New version coming soon! Please checkout **New Features** below.)

**NOTICE**
Remeber to set locale in environment
```
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export PYTHONIOENCODING=UTF-8
```

## INDEX: 
1. [TWCC-CLI α for v0.5](https://github.com/TW-NCHC/TWCC-CLI/tree/v0.5) | [@PYPI](https://pypi.org/project/TWCC-CLI/) | [User Manual](https://man.twcc.ai/@twccdocs/twcc-cli-v05)

1. Release Notes :point_down:

```
Sorry! In order to provide better user experience, the TWCC CLI new version launch of this week will delay a week.

by twcc-cli-team on May 22
```

### v0.5.11 Release Note
![img](https://media.giphy.com/media/y6T75vNWBQzCg/giphy.gif)
**change**
- In v0.5.10, we use `--product-type` in wrong place, that has been correct.
- We change `cp cos` command structures, new command  descriptions as following:
```bash=
> twccli cp cos --help
Usage: twccli cp cos [OPTIONS]

  ‘Upload/Download’ COS (Cloud Object Storage) files.

Options:
  -upload                   Upload files or folders to the bucket.
  -download                 Download files from the bucket or download the
                            entire bucket.
  -src, --source TEXT       Path of the source directory.
  -okey, --object-key TEXT  File in Cloud.
  -fn, --file-name TEXT     Files for uploading from local site.
  -bkt, --bucket-name TEXT  Upload files or folders to the bucket.
  --help                    Show this message and exit.

```

**discuss**
- We are trying to laverage [Ansible](https://www.ansible.com/) for deloying any services. 
Do you have any suggestions to this? 
Welcome to [leave comments](https://github.com/TW-NCHC/TWCC-CLI/issues/new!!


 
### v0.5.10 Release Note
![img](https://media.giphy.com/media/xTiTntKyFNFbCNuqkw/giphy.gif)
**change**
- VCS images showing table shows "product-type" now!

### v0.5.9 Release Note

![img](https://media.giphy.com/media/l3V0oNVYGk3Sx9N60/giphy.gif)

**change**
- orginal `-itype` in `ls vcs` and `mk vcs` change to using `-ptype` and `--product-type`.

**fix bug**
- error in `rm vcs -secg` and `ls vcs -img` with filtering.
- error in `cp cos -upload` , `cp cos -download` and `rm cos` bucket.


### v0.5.7 Release Note
![img](https://media.giphy.com/media/dQpUkK59l5Imxsh8jN/giphy.gif)


** We have updated our document in [TWCC-CLI α for v0.5](https://man.twcc.ai/@twccdocs/twcc-cli-v05)


**fix bug**
- fix bugs in COS and data-vol-type while creating VCS.

### v0.5.6 Release Note
![img](https://media.giphy.com/media/xUA7b7yLPq3IPOLnk4/giphy.gif)

**new features**
- You can create additional data volume in `ssd` and `ssd-encrypt` type.

**fix bug**
- upload file source path with slash is not work.
- adding error condition in `rm ccs -s` while entering resource name, and adding `-s` parameter in `ls ccs`.
- fix naming standard to 6-16 in length.
- support customized clone image in CCS.

### v0.5.5 Release Note
![img](https://media.giphy.com/media/xThuWmOkO0SvRprLXy/giphy.gif)


**new features**
- snapshot delete functions, `twccli rm vsc -snap -snap-id $SNAPTSHOT_ID`

**fix bug**
- delete bucket and file operation
- upload and download dir to bucket
- remove flag 'noforce' in `twccli rm`
- update listing all snapshots for Project Owner
- `rm vcs` with `-s` flag

### v0.5.4 Release Note
![img](https://media.giphy.com/media/MtIPR6C5okdt6/giphy.gif)


**new features**
- provides encoding setting, `twccli config init --set-bashrc`

**fix bug**
- no data while listing VCS 
- can't delete bucket with data recursively
- can't download hierarchy directory to local site 
- modify parameter and description in command "CP"

### v0.5.3 Release Note

![img](https://media.giphy.com/media/xHMIDAy1qkzNS/giphy.gif)

**new features**
- We add encoding environ setting
- add keypair write and del file
- add private ip and network info while ls vcs

**fix**
- fix create keypair's bug
- fix error in `MANIFEST.in`, remove vcs cos, list vcs, --help description of cos


### v0.5.2 Release Note
**New and structured CLI commands!**

for Mar. 20th ,2020 (v0.5.2)
  - Now you can use structured commands`config`, `mk`, `ls`, `rm`, `cp`, and `net` to customize and manage your TWCC Compute and Storage services, including VCS, CCS, and COS.
  - In addition to CCS and COS, now you can use TWCC CLI to manage your VCS resources, including VCS instances, security groups, snapshots, as well as keypairs.
  - Use commands`-table` or `-json show` to clearly diaplay your resource information in a table view or in JSON.


## Contact us
If you have any questions, please email us at: 
- iservice@narlabs.org.tw for account support
- isupport@narlabs.org.tw for technical support
