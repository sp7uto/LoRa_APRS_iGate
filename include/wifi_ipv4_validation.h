// SPDX-License-Identifier: GPL-3.0-or-later
#pragma once
#include <stdint.h>
namespace wifi_ipv4 {
inline bool parse(const char* text, uint32_t& out) {
    if (!text) return false;
    uint32_t result = 0;
    for (int part = 0; part < 4; ++part) {
        unsigned v = 0, digits = 0;
        while (*text >= '0' && *text <= '9') {
            v = v * 10 + unsigned(*text++ - '0');
            if (++digits > 3 || v > 255) return false;
        }
        if (!digits) return false;
        result = (result << 8) | v;
        if (part < 3 && *text++ != '.') return false;
    }
    if (*text) return false;
    out = result;
    return true;
}
inline bool unicast(uint32_t a) {
    const uint32_t first = a >> 24;
    return first != 0 && first != 127 && first < 224;
}
inline bool validProfile(const char* ip, const char* gateway, const char* subnet,
                         const char* dns1, const char* dns2) {
    uint32_t a, g, m, d, e;
    if (!parse(ip,a) || !parse(gateway,g) || !parse(subnet,m) || !parse(dns1,d))
        return false;
    if (!unicast(a) || !unicast(g) || !unicast(d) || a == g) return false;
    if (dns2 && *dns2 && (!parse(dns2,e) || !unicast(e))) return false;
    const uint32_t host = ~m;
    // Require contiguous /1 through /30, a usable LAN host and same-subnet gateway.
    if (m == 0 || host < 3 || (host & (host + 1)) != 0) return false;
    if ((a & m) != (g & m)) return false;
    return (a & host) != 0 && (a & host) != host &&
           (g & host) != 0 && (g & host) != host;
}
} // namespace wifi_ipv4
