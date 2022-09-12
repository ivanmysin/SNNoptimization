#include "code_objects/neurongroup_stateupdater_codeobject.h"
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



void _run_neurongroup_stateupdater_codeobject()
{
    using namespace brian;


    ///// CONSTANTS ///////////
    const double EL = - 0.065;
const double gL = 0.0001;
const int64_t N = 1;
const size_t _numdt = 1;
const double gbarKdr = 0.009000000000000001;
const double Cm = 1e-06;
const double ENa = 0.055;
const double EK = - 0.09;
const double ms = 0.001;
const double gbarNa = 0.035;
const double mV = 0.001;
const double Iapp = 2e-06;
const size_t _numh = 1;
const size_t _numv = 1;
const size_t _numn = 1;
    ///// POINTERS ////////////
        
    double*   _ptr_array_defaultclock_dt = _array_defaultclock_dt;
    double*   _ptr_array_neurongroup_h = _array_neurongroup_h;
    double*   _ptr_array_neurongroup_v = _array_neurongroup_v;
    double*   _ptr_array_neurongroup_n = _array_neurongroup_n;


    //// MAIN CODE ////////////
    // scalar code
    const size_t _vectorisation_idx = -1;
        
    const double dt = _ptr_array_defaultclock_dt[0];
    const double _lio_1 = 1.0f*0.019258127019742523/ms;
    const double _lio_2 = 1.0f*0.05/mV;
    const double _lio_3 = 0.060810062625218 * ms;
    const double _lio_4 = 1.0f*(- 0.1)/mV;
    const double _lio_5 = 1.0f*1.0/mV;
    const double _lio_6 = 1.0f*0.5/ms;
    const double _lio_7 = 1.0f*(- 0.5)/ms;
    const double _lio_8 = 1.0f*0.1/mV;
    const double _lio_9 = 1.0f*0.36059363148780416/ms;
    const double _lio_10 = (1.0f*(EL * gL)/Cm) + (1.0f*Iapp/Cm);
    const double _lio_11 = 0.015625 * (ENa * gbarNa);
    const double _lio_12 = 0.015625 * Cm;
    const double _lio_13 = Cm * 4.5399929762484854e-05;
    const double _lio_14 = 1.0f*0.16666666666666666/mV;
    const double _lio_15 = 0.75 * (Cm * 0.001272633801339809);
    const double _lio_16 = 1.0f*0.1111111111111111/mV;
    const double _lio_17 = 0.1875 * (Cm * 0.03567399334725241);
    const double _lio_18 = 1.0f*0.05555555555555555/mV;
    const double _lio_19 = 1.0f*(EK * gbarKdr)/Cm;
    const double _lio_20 = 0.0 - (1.0f*gL/Cm);
    const double _lio_21 = (- 0.015625) * gbarNa;
    const double _lio_22 = 1.0f*gbarKdr/Cm;


    const int _N = N;
    
    for(int _idx=0; _idx<_N; _idx++)
    {
        // vector code
        const size_t _vectorisation_idx = _idx;
                
        double h = _ptr_array_neurongroup_h[_idx];
        double v = _ptr_array_neurongroup_v[_idx];
        double n = _ptr_array_neurongroup_n[_idx];
        const double _BA_h = 1.0f*(_lio_1 * exp(_lio_2 * (- v)))/((1.0f*(- 5.0)/(ms + (_lio_3 * exp(_lio_4 * v)))) - (1.0f*_lio_1/(_brian_pow(exp(_lio_5 * v), 0.05))));
        const double _h = (- _BA_h) + ((_BA_h + h) * exp(dt * ((1.0f*(- 5.0)/(ms + (_lio_3 * exp(_lio_4 * v)))) - (1.0f*_lio_1/(_brian_pow(exp(_lio_5 * v), 0.05))))));
        const double _BA_n = 1.0f*_lio_6/(((1.0f*_lio_7/_exprel((- 3.4000000000000004) - (_lio_8 * v))) - (1.0f*_lio_9/(_brian_pow(exp(_lio_5 * v), 0.0125)))) * _exprel((- 3.4000000000000004) - (_lio_8 * v)));
        const double _n = (- _BA_n) + ((_BA_n + n) * exp(dt * ((1.0f*_lio_7/_exprel((- 3.4000000000000004) - (_lio_8 * v))) - (1.0f*_lio_9/(_brian_pow(exp(_lio_5 * v), 0.0125))))));
        const double _BA_v = 1.0f*(_lio_10 + ((1.0f*(_lio_11 * h)/(_lio_12 + (((_lio_13 * (exp(_lio_14 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 3)))) + (_lio_15 * (exp(_lio_16 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 2))))) + (_lio_17 * (exp(_lio_18 * (- v)) * _exprel((- 3.5) - (_lio_8 * v))))))) + (_lio_19 * (_brian_pow(n, 4)))))/((_lio_20 + (1.0f*(_lio_21 * h)/(_lio_12 + (((_lio_13 * (exp(_lio_14 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 3)))) + (_lio_15 * (exp(_lio_16 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 2))))) + (_lio_17 * (exp(_lio_18 * (- v)) * _exprel((- 3.5) - (_lio_8 * v)))))))) - (_lio_22 * (_brian_pow(n, 4))));
        const double _v = (- _BA_v) + ((_BA_v + v) * exp(dt * ((_lio_20 + (1.0f*(_lio_21 * h)/(_lio_12 + (((_lio_13 * (exp(_lio_14 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 3)))) + (_lio_15 * (exp(_lio_16 * (- v)) * (_brian_pow(_exprel((- 3.5) - (_lio_8 * v)), 2))))) + (_lio_17 * (exp(_lio_18 * (- v)) * _exprel((- 3.5) - (_lio_8 * v)))))))) - (_lio_22 * (_brian_pow(n, 4))))));
        h = _h;
        n = _n;
        v = _v;
        _ptr_array_neurongroup_h[_idx] = h;
        _ptr_array_neurongroup_v[_idx] = v;
        _ptr_array_neurongroup_n[_idx] = n;

    }

}


