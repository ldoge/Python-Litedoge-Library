# Copyright (C) 2012-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

class MainParams(bitcoin.core.CoreChainParams):
    MESSAGE_START = b'\xa1\xa0\xa2\xa3'
    DEFAULT_PORT = 50990
    RPC_PORT = 51990
    DNS_SEEDS = (('opal-coin.com', 'seed.opal-coin.com'),
                 ('opal-coin.com', 'seeder1.opal-coin.com'),
                 ('opal-coin.com', 'seeder2.opal-coin.com'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':115,
                       'SCRIPT_ADDR':28,
                       'SECRET_KEY' :128}

"""
class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\xa1\xa0\xa2\xa3'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('bitcoin.petertodd.org', 'testnet-seed.bitcoin.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
"""
"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
#    elif name == 'testnet':
#        params = bitcoin.core.coreparams = TestNetParams()
#    elif name == 'regtest':
#        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
