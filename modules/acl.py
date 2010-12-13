'''
acl.py
ACL - Access Control List
'''

from copy import copy
from datetime import datetime
import os

# the db file name
ACL_DB_FILE = 'acl.db'

# channel to admin mapping
ACL_CHANADMINS = {
        '##uno' : ['Kays'],
}

# does the server have NickServ? 
NICKSERV_ON = True


## DO NOT EDIT BELOW THIS LINE UNLESS YOU *KNOW* WHAT YOU'RE DOING! ##
CHAN_OPERATOR               = 0x00000001
CHAN_HALFOP                 = 0x00000002
CHAN_VOICE                  = 0x00000004
CHAN_GRANT_VOICE            = 0x00000008
CHAN_GRANT_HALFOP           = 0x00000010
CHAN_GRANT_OPERATOR         = 0x00000020
CHAN_PERM_ALL               = CHAN_OPERATOR | CHAN_HALF_OPERATOR | CHAN_VOICE
CHAN_GRANT_ALL              = CHAN_GRANT_VOICE | CHAN_GRANT_HALFOP | CHAN_GRANT_OPERATOR
CHAN_ALL                    = CHAN_PERM_ALL | CHAN_GRANT_ALL

ACL_FLAGS = { }

ACL_STR = {
    'INSUFFICIENT_PRIVS'    :   'You do not have the privileges to execute this command.',
    'INSUFFICIENT_ARGS_ADD' :   'Syntax: .acl add [#chan] <name> <usermask> [-|+]<flags>',
    'INSUFFICIENT_ARGS_DEL' :   'Syntax: .acl del [#chan] <name> <usermask> [-|+]<flags>',
    'USER_ALREADY_EXISTS' :   'User %s already exists.',
}

def set_flags (chan, user, flags):
    if not ACL_FLAGS.has_key(chan):
        ACL_FLAGS[chan] = {}
    if not ACL_FLAGS[chan].has_key(user):
        f = getFlags(ACL_FLAGS[chan][user], flags)
        ACL_FLAGS[chan][user] = f
    else:
        f = getFlags(ACL_FLAGS[chan][user], flags)
        ACL_FLAGS[chan][user] = f

def getFlags (userflags, modflags):
    m = len(modflags)
    n = 0
    dir = 0
    while n < m:
        i = modflags[n]
        if i == '+':
            dir = 0
        elif i == '-':
            dir = 1
        elif i == '*':
            if dir: userflags = 0
            else: userflags = CHAN_ALL
        elif i == 'o':
            if dir: userflags &= ~CHAN_OPERATOR
            else: userflags |= CHAN_OPERATOR
        elif i == 'h':
            if dir: userflags &= ~CHAN_HALFOP
            else: userflags |= CHAN_HALFOP
        elif i == 'v':
            if dir: userflags &= ~CHAN_VOICE
            else: userflags |= CHAN_VOICE
        elif i == 'V':
            if dir: userflags &= ~CHAN_GRANT_VOICE
            else: userflags |= CHAN_GRANT_VOICE
        elif i == 'H':
            if dir: userflags &= ~CHAN_GRANT_HALFOP
            else: userflags |= CHAN_GRANT_HALFOP
        elif i == 'O':
            if dir: userflags &= ~CHAN_GRANT_OPERATOR
            else: userflags |= CHAN_GRANT_OPERATOR
        else: break
        n += 1
    return userflags


## BELOW THIS LINE -- WORK IN PROGRESS ##
def can_acl_add (nick):
    if input.nick in jenney.config.admins: return 1
    if input.nick in ACL_FLAGS[chan][user]


def acl_add (jenney, input):
    # if input.nick is not an admin, fail!
    if not can_acl_add(input.nick):
        jenney.notice(input.nick, ACL_STR['INSUFFICIENT_PRIVS'])
        return

    args = input.group().split()
    lenArgs = len(args)
    if lenArgs < 5:
        jenney.notice(input.nick, ACL_STR['INSUFFICIENT_ARGS_ADD'])

    chan = input.sender
    jname = args[2]
    jmask = args[3]
    jflags = args[4]
    nparams = 5
    if args[2].startswith('#'):
        if lenArgs < 6:
            jenney.notice(input.nick, ACL_STR['INSUFFICIENT_ARGS_ADD'])
            return
        chan = args[2]
        jname = args[3]
        jmask = args[4]
        jflags = args[5]

    if lenArgs < nparams:
        jenney.notice(input.nick, ACL_STR['INSUFFICIENT_ARGS_ADD'])
        return
    elif ACL_FLAGS.has_key(chan):
        if ACL_C[chan].has_key(
        jenney.notice(input.nick, ACL_STR['USER_ALREADY_EXISTS'] % args[2])
        return

def create_db_if_not_exists ():
    if not db_file_exists():
        f = open(ACL_DB_FILE, 'w')
        f.close()

def db_file_exists ():
    return os.path.exists(ACL_DB_FILE)

if __name__ == '__main__':
    print __doc__.strip()
