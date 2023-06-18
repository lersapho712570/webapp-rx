# This MD page
##### lsblk

```bash
root@ubuntu20:~# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                         8:0    0   16G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    1G  0 part /boot
└─sda3                      8:3    0   15G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0    4G  0 lvm  /

```

##### fdisk

```bash
fdisk -l
fdisk /dev/sdb
m - help
p - print
n - n
d - delete
```
