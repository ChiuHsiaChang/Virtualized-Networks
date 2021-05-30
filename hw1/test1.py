"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

# class MyTopo( Topo ):
#     "Simple topology example."

#     def build( self ):
#         "Create custom topo."

#         # Add hosts and switches
#         leftHost = self.addHost( 'h1' )
#         rightHost = self.addHost( 'h2' )
#         leftSwitch = self.addSwitch( 's3' )
#         rightSwitch = self.addSwitch( 's4' )

#         # Add links
#         self.addLink( leftHost, leftSwitch )
#         self.addLink( leftSwitch, rightSwitch )
#         self.addLink( rightSwitch, rightHost )


# topos = { 'mytopo': ( lambda: MyTopo() ) }

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        midHost = self.addHost( 'h2' )
        rightHost = self.addHost( 'h3' )
        leftSwitch = self.addSwitch( 's1' )
        midSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( midHost, midSwitch )
        self.addLink( rightSwitch, rightHost )
        self.addLink( rightSwitch, midSwitch )
        self.addLink( midSwitch, leftSwitch )
        self.addLink( rightSwitch, leftSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
