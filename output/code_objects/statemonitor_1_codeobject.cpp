#include "code_objects/statemonitor_1_codeobject.h"
#include "objects.h"
#include "brianlib/common_math.h"
#include "brianlib/stdint_compat.h"
#include<cmath>
#include<ctime>
#include<iostream>
#include<fstream>
#include<climits>

////// SUPPORT CODE ///////
namespace {
        
    static inline double _exprel(double x)
    {
        if (fabs(x) < 1e-16)
            return 1.0;
        if (x > 717)
            return INFINITY;
        return expm1(x)/x;
    }
    template < typename T1, typename T2 > struct _higher_type;
    template < > struct _higher_type<int,int> { typedef int type; };
    template < > struct _higher_type<int,long> { typedef long type; };
    template < > struct _higher_type<int,long long> { typedef long long type; };
    template < > struct _higher_type<int,float> { typedef float type; };
    template < > struct _higher_type<int,double> { typedef double type; };
    template < > struct _higher_type<int,long double> { typedef long double type; };
    template < > struct _higher_type<long,int> { typedef long type; };
    template < > struct _higher_type<long,long> { typedef long type; };
    template < > struct _higher_type<long,long long> { typedef long long type; };
    template < > struct _higher_type<long,float> { typedef float type; };
    template < > struct _higher_type<long,double> { typedef double type; };
    template < > struct _higher_type<long,long double> { typedef long double type; };
    template < > struct _higher_type<long long,int> { typedef long long type; };
    template < > struct _higher_type<long long,long> { typedef long long type; };
    template < > struct _higher_type<long long,long long> { typedef long long type; };
    template < > struct _higher_type<long long,float> { typedef float type; };
    template < > struct _higher_type<long long,double> { typedef double type; };
    template < > struct _higher_type<long long,long double> { typedef long double type; };
    template < > struct _higher_type<float,int> { typedef float type; };
    template < > struct _higher_type<float,long> { typedef float type; };
    template < > struct _higher_type<float,long long> { typedef float type; };
    template < > struct _higher_type<float,float> { typedef float type; };
    template < > struct _higher_type<float,double> { typedef double type; };
    template < > struct _higher_type<float,long double> { typedef long double type; };
    template < > struct _higher_type<double,int> { typedef double type; };
    template < > struct _higher_type<double,long> { typedef double type; };
    template < > struct _higher_type<double,long long> { typedef double type; };
    template < > struct _higher_type<double,float> { typedef double type; };
    template < > struct _higher_type<double,double> { typedef double type; };
    template < > struct _higher_type<double,long double> { typedef long double type; };
    template < > struct _higher_type<long double,int> { typedef long double type; };
    template < > struct _higher_type<long double,long> { typedef long double type; };
    template < > struct _higher_type<long double,long long> { typedef long double type; };
    template < > struct _higher_type<long double,float> { typedef long double type; };
    template < > struct _higher_type<long double,double> { typedef long double type; };
    template < > struct _higher_type<long double,long double> { typedef long double type; };
    template < typename T1, typename T2 >
    static inline typename _higher_type<T1,T2>::type
    _brian_mod(T1 x, T2 y)
    {{
        return x-y*floor(1.0*x/y);
    }}
    template < typename T1, typename T2 >
    static inline typename _higher_type<T1,T2>::type
    _brian_floordiv(T1 x, T2 y)
    {{
        return floor(1.0*x/y);
    }}
    #ifdef _MSC_VER
    #define _brian_pow(x, y) (pow((double)(x), (y)))
    #else
    #define _brian_pow(x, y) (pow((x), (y)))
    #endif

}

////// HASH DEFINES ///////



void _run_statemonitor_1_codeobject()
{
    using namespace brian;


    ///// CONSTANTS ///////////
    const size_t _num__source_gNa_neurongroup_h = 1;
const double ms = 0.001;
const size_t _num____source_gNa_neurongroup_m_neurongroup_alpha_m_neurongroup_v = 1;
const size_t _num_clock_t = 1;
const size_t _numN = 1;
const double mV = 0.001;
const double gbarNa = 0.035;
const size_t _num_indices = 1;
double* const _array_statemonitor_1_t = _dynamic_array_statemonitor_1_t.empty()? 0 : &_dynamic_array_statemonitor_1_t[0];
const size_t _numt = _dynamic_array_statemonitor_1_t.size();
const size_t _num____source_gNa_neurongroup_m_neurongroup_beta_m_neurongroup_v = 1;
    ///// POINTERS ////////////
        
    double*   _ptr_array_neurongroup_h = _array_neurongroup_h;
    double*   _ptr_array_neurongroup_v = _array_neurongroup_v;
    double*   _ptr_array_defaultclock_t = _array_defaultclock_t;
    int32_t*   _ptr_array_statemonitor_1_N = _array_statemonitor_1_N;
    int32_t*   _ptr_array_statemonitor_1__indices = _array_statemonitor_1__indices;
    double* __restrict  _ptr_array_statemonitor_1_t = _array_statemonitor_1_t;


    _dynamic_array_statemonitor_1_t.push_back(_ptr_array_defaultclock_t[0]);

    const size_t _new_size = _dynamic_array_statemonitor_1_t.size();
    // Resize the dynamic arrays
    _dynamic_array_statemonitor_1_gNa.resize(_new_size, _num_indices);

    // scalar code
    const size_t _vectorisation_idx = -1;
        
    const double _lio_1 = 1.0f*1.0/ms;
    const double _lio_2 = 1.0f*0.1/mV;
    const double _lio_3 = 35.0 * mV;
    const double _lio_4 = 1.0f*4.0/ms;
    const double _lio_5 = 1.0f*0.05555555555555555/mV;
    const double _lio_6 = 60.0 * mV;


    
    for (int _i = 0; _i < (int)_num_indices; _i++)
    {
        // vector code
        const size_t _idx = _ptr_array_statemonitor_1__indices[_i];
        const size_t _vectorisation_idx = _idx;
                
        const double ____source_gNa_neurongroup_m_neurongroup_alpha_m_neurongroup_v = _ptr_array_neurongroup_v[_idx];
        const double __source_gNa_neurongroup_h = _ptr_array_neurongroup_h[_idx];
        const double ____source_gNa_neurongroup_m_neurongroup_beta_m_neurongroup_v = _ptr_array_neurongroup_v[_idx];
        const double ___source_gNa_neurongroup_m_neurongroup_alpha_m = 1.0f*_lio_1/_exprel(_lio_2 * (- (_lio_3 + ____source_gNa_neurongroup_m_neurongroup_alpha_m_neurongroup_v)));
        const double ___source_gNa_neurongroup_m_neurongroup_beta_m = _lio_4 * exp(_lio_5 * (- (_lio_6 + ____source_gNa_neurongroup_m_neurongroup_beta_m_neurongroup_v)));
        const double __source_gNa_neurongroup_m = 1.0f*___source_gNa_neurongroup_m_neurongroup_alpha_m/(___source_gNa_neurongroup_m_neurongroup_alpha_m + ___source_gNa_neurongroup_m_neurongroup_beta_m);
        const double _source_gNa = gbarNa * ((_brian_pow(__source_gNa_neurongroup_m, 3)) * __source_gNa_neurongroup_h);
        const double _to_record_gNa = _source_gNa;


        _dynamic_array_statemonitor_1_gNa(_new_size-1, _i) = _to_record_gNa;
    }

    _ptr_array_statemonitor_1_N[0] = _new_size;


}


