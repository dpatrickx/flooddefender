package net.floodlightcontroller.statistics;

import org.projectfloodlight.openflow.types.OFPort;

public class ActionEntry {
	OFPort port;
	int passed;
	
	public ActionEntry() {
		passed = 0;
		port = OFPort.of(0);
	}
	public ActionEntry(OFPort p) {
		passed = 0;
		port = p;
	}
	OFPort pass() {
		passed = 1;
		return port;
	}
}
