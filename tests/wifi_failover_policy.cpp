// SPDX-License-Identifier: GPL-3.0-or-later
#include "wifi_failover_policy.h"
#include <cassert>
int main() {
    wifi_failover::Policy p;
    assert(!p.observe(0,false,false));
    assert(!p.observe(100,true,false));
    assert(!p.observe(180099,true,false));
    assert(p.observe(180100,true,false));
    assert(!p.observe(180101,true,false));
    assert(!p.observe(360101,true,false));
    assert(!p.observe(480099,true,false));
    assert(p.observe(480100,true,false));
    assert(!p.observe(480101,true,false));
    assert(!p.observe(600000,true,true));
    assert(!p.observe(700000,true,false));
    assert(!p.observe(879999,true,false));
    assert(p.observe(880000,true,false));
    wifi_failover::Policy wrap;
    const uint32_t start = 0xfffffff0u;
    assert(!wrap.observe(start,true,false));
    assert(wrap.observe(uint32_t(start+180000u),true,false));
}
