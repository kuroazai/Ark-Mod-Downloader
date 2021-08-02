# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:52:15 2021

@author: KuroAzai

For those unfortunate epic gamers owners who have ark here's smol solution
"""
import os
import glob
import shutil


class pathmanager():

    def __init__(self):
        # location of your ark cotent/mods
        self.moddir = r'C:\Users\Odin\Documents\mods'
        # location of your steam directory
        self.steamcddir = r'L:\Steamcd'


def download_mods():
    '''
    Downloads mods with steam cmd ~

    Returns
    -------
    None.

    '''
    # change to steamcd dir
    os.chdir(PM.steamcddir)
    # run the new file we created haha
    os.system('steamcmd.exe +runscript arkmods.txt')
    # wait and suffer until it's done


def install_mods():
    '''
    transfers files into your game directory
    run the game after for it to finish installation

    Returns
    -------
    None.

    '''
    staging = PM.steamcddir + r'\steamapps\workshop\content\346110'
    file = PM.steamcddir + r'\steamapps\workshop\content\346110\{}\WindowsNoEditor'
    paths = glob.glob(staging + r'\*')

    for x in paths:
        modid = x.replace(staging, '')[1:]
        source = file.format(modid)
        targetloc = PM.moddir + r'\{}'.format(modid)
        shutil.move(source, targetloc)
        os.remove(file.replace(r'\WindowsNoEditor', ''))
        print('Moved', modid, source)


def process_mods():
    '''
    processes a modlist and builds commands to
    download/update your mods

    Returns
    -------
    None.

    '''
    print('processing')
    # cmd
    start_cmd = 'login anonymous '
    end_cmd = 'quit'
    cmd = 'workshop_download_item 346110'
    cmds = []
    with open('mods.txt', 'r') as f:
        mods = f.read()
        mods = mods.replace(',', '\n')
        mods = mods.splitlines()
        for x in mods:
            cmds.append('\n' + cmd + ' ' + x)
            start_cmd += '\n' + cmd + ' ' + x
    start_cmd += '\n' + end_cmd
    with open(PM.steamcddir + '/arkmods.txt', 'w+') as f:
        f.write(start_cmd)


def main():
    process_mods()
    download_mods()
    install_mods()
    print('Jobs Done!!')


if __name__ == "__main__":
    PM = pathmanager()
    main()
