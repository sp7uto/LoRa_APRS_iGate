// SPDX-License-Identifier: GPL-3.0-or-later
#include "wifi_ipv4_validation.h"
#include <cassert>
int main() {
    using wifi_ipv4::validProfile;
    assert(validProfile("192.168.1.50","192.168.1.1","255.255.255.0","9.9.9.9",""));
    assert(validProfile("10.0.0.2","10.0.0.1","255.255.255.252","1.1.1.1","9.9.9.9"));
    assert(!validProfile("192.168.1.256","192.168.1.1","255.255.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.0","192.168.1.1","255.255.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.255","192.168.1.1","255.255.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.50","192.168.2.1","255.255.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.50","192.168.1.1","255.0.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.50","192.168.1.50","255.255.255.0","9.9.9.9",""));
    assert(!validProfile("192.168.1.50","192.168.1.1","255.255.255.0","0.0.0.0",""));
    assert(!validProfile("192.168.1.50","192.168.1.1","255.255.255.0","9.9.9.9","999.1.1.1"));
    uint32_t v;
    assert(!wifi_ipv4::parse("1.2.3",v));
    assert(!wifi_ipv4::parse("1.2.3.4 ",v));
    assert(!wifi_ipv4::parse("1..3.4",v));
}
