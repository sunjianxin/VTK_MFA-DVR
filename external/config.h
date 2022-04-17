#include <vector>

#define SHADEON
// #define TIME
#define THREADID 0
// #define PROFILE
// #define GRADIENT_VTK
// #define VALUE_VTK
// #define SKIPUPDATINGSHADINGTABLE

struct sample {
    int j; // row index
    int i; // column index
    double x; // x location
    double y; // x location
    double z; // x location
    double v_linear; // value
    double v_mfa; // value
};
