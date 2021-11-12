#include <cstdint>
#include "MAC_VEC.hpp"

extern "C" {
    void MAC_VEC_FP32(uint32_t size, float a[], float x[], float b[], float y[]){
        MAC_VEC::mac_vec<float>(size, a, x, b, y);
    }
    void MAC_VEC_INT16(uint32_t size, int16_t a[], int16_t x[], int16_t b[], int16_t y[]){
        MAC_VEC::mac_vec<int16_t>(size, a, x, b, y);
    }
    void MAC_VEC_UINT32(uint32_t size, uint32_t a[], uint32_t x[], uint32_t b[], uint32_t y[]){
        MAC_VEC::mac_vec<uint32_t>(size, a, x, b, y);
    }
}
