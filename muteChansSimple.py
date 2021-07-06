from maya import cmds
def getSelectedChannels():
    if not cmds.ls(sl=True):
        return
    gChannelBoxName = mel.eval('$temp=$gChannelBoxName')
    sma = cmds.channelBox(gChannelBoxName, query=True, sma=True)
    ssa = cmds.channelBox(gChannelBoxName, query=True, ssa=True)
    sha = cmds.channelBox(gChannelBoxName, query=True, sha=True)
    channels = list()
    if sma:
        channels.extend(sma)
    if ssa:
        channels.extend(ssa)
    if sha:
        channels.extend(sha)
    return channels 
chans = getSelectedChannels()

if not chans:
    objs = cmds.ls(sl=True)
    attrsObjs = cmds.listAttr(objs, keyable=True, u=True, v=True)
    muteState = cmds.mute('{}.{}'.format(objs[0], attrsObjs[0]), q=True)
    if not muteState:
        cmds.mute(objs, force=True)
    else:
        cmds.mute(objs, disable=True, force=True)
else:
    attrsToMute = []
    objs = cmds.ls(sl=True)
    for obj in objs:
        for chan in chans:
            attr = '{}.{}'.format(obj, chan)
            attrsToMute.append(attr)
    muteState = cmds.mute(attrsToMute[0], q=True)
    if not muteState:
        cmds.mute(attrsToMute, force=True)
    else:
        cmds.mute(attrsToMute, disable=True, force=True)
