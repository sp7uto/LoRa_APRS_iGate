// SPDX-License-Identifier: GPL-3.0-or-later
#pragma once
#include <stdint.h>
namespace wifi_failover {
class Policy {
    bool tracking = false;
    bool switched = false;
    uint32_t unhealthySince = 0;
    uint32_t lastSwitch = 0;
public:
    bool observe(uint32_t now, bool eligible, bool healthy) {
        if (!eligible || healthy) { tracking = false; return false; }
        if (!tracking) { tracking = true; unhealthySince = now; return false; }
        if (now - unhealthySince < 180000UL) return false;
        if (switched && now - lastSwitch < 300000UL) return false;
        switched = true;
        lastSwitch = now;
        tracking = false;
        return true;
    }
};
}
