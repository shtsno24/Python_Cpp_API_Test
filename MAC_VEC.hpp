#include <cstdint>

namespace MAC_VEC{
    template<typename data_t>
    void mac_vec(uint32_t size, data_t a[], data_t x[], data_t b[], data_t y[]){
        for(uint32_t i = 0; i < size; i++){
            y[i] = a[i] * x[i] + b[i];
        }
    }
}
