// This program executes exceptionally well with Art Tatum's 'Night and Day' or 'Humoresque' as background music.
// About 58% of this code was written with my cat, Spike, sitting on my lap.

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <cmath>
#include <time.h>
#include "headers/matplotlibcpp.h"

using namespace std;
namespace plt = matplotlibcpp;

struct components
{
   int a, b, c;
};

/*
float est_time(int x) {
    float t = (-6.61757 * pow(10, -16) * pow(x, 4))
            + (3.27884 * pow(10, -11) * pow(x, 3))
            + (1.41993 * pow(10, -7) * pow(x, 2))
            + (0.000389968 * x)
            + 5;
    return  t;
}
*/


void problem_function( double *F, double *G, double *X);
/***********************************************************************/
extern"C"{ int midaco(long int*,long int*,long int*,long int*,long int*,
                      long int*,double*,double*,double*,double*,double*,
                      long int*,long int*,double*,double*,long int*,
                      long int*,long int*,double*,long int*,char*);}
/***********************************************************************/
extern"C"{ int midaco_print(int,long int,long int,long int*,long int*,double*,
                            double*,double*,double*,double*,long int,long int,
                            long int,long int,long int,double*,double*,
                            long int,long int,double*,long int,char*);}

void problem_function( double *f, double *g, double *x, int val )
{
    /* Objective functions F(X) */
    f[0] = ((pow(4, x[0]))*((8*x[1])+7)) - val;

    /* Equality constraints G(X) = 0 MUST COME FIRST in g[0:me-1] */
    g[0] = ((pow(4, x[0]))*((8*x[1])+7)) - val;  // = 0

    /* Inequality constraints G(X) >= 0 MUST COME SECOND in g[me:m-1] */
    g[1] = x[0]; // >= 0
    g[2] = x[1]; // >= 0
}


int solve(int val)
{
      /* Variable and Workspace Declarations */
      long int o,n,ni,m,me,maxeval,maxtime,printeval,save2file,iflag,istop;
      long int liw,lrw,lpf,i,iw[5000],p=1; double rw[20000],pf[20000];
      double   f[10],g[1000],x[1000],xl[1000],xu[1000],param[13];
      char key[] = "MIDACO_LIMITED_VERSION___[CREATIVE_COMMONS_BY-NC-ND_LICENSE]";

      /*****************************************************************/
      /***  Step 1: Problem definition  ********************************/
      /*****************************************************************/

      /* STEP 1.A: Problem dimensions
      ******************************/
      o  = 1; /* Number of objectives                          */
      n  = 2; /* Number of variables (in total)                */
      ni = 2; /* Number of integer variables (0 <= ni <= n)    */
      m  = 3; /* Number of constraints (in total)              */
      me = 1; /* Number of equality constraints (0 <= me <= m) */

      /* STEP 1.B: Lower and upper bounds 'xl' & 'xu'
      **********************************************/
      for( i=0; i<n; i++)
      {
         xl[i] = 0;
         xu[i] = val;
      }

      /* STEP 1.C: Starting point 'x'
      ******************************/
      for( i=0; i<n; i++)
      {
         x[i] = xl[i]; /* Here for example: starting point = lower bounds */
      }

      /*****************************************************************/
      /***  Step 2: Choose stopping criteria and printing options   ****/
      /*****************************************************************/

      /* STEP 2.A: Stopping criteria
      *****************************/
      maxeval = 1000;    /* Maximum number of function evaluation (e.g. 1000000)  */
      maxtime = 60*60*24; /* Maximum time limit in Seconds (e.g. 1 Day = 60*60*24) */

      /* STEP 2.B: Printing options
      ****************************/
      printeval = 1000; /* Print-Frequency for current best solution (e.g. 1000) */
      save2file = 1;    /* Save SCREEN and SOLUTION to TXT-files [ 0=NO/ 1=YES]  */

      /*************************************************************************/
      /***  Step 3: Choose MIDACO parameters (FOR ADVANCED USERS) (not me)   ***/
      /*************************************************************************/

      param[ 0] =  0.0;  /* ACCURACY  */
      param[ 1] =  0.0;  /* SEED      */
      param[ 2] =  0.0;  /* FSTOP     */
      param[ 3] =  0.0;  /* ALGOSTOP  */
      param[ 4] =  0.0;  /* EVALSTOP  */
      param[ 5] =  0.0;  /* FOCUS     */
      param[ 6] =  0.0;  /* ANTS      */
      param[ 7] =  0.0;  /* KERNEL    */
      param[ 8] =  0.0;  /* ORACLE    */
      param[ 9] =  0.0;  /* PARETOMAX */
      param[10] =  0.0;  /* EPSILON   */
      param[11] =  0.0;  /* BALANCE   */
      param[12] =  0.0;  /* CHARACTER */

      /*****************************************************************/
      /*
         Call MIDACO by Reverse Communication
      */
      /*****************************************************************/
      /* Workspace length calculation */
      lrw=sizeof(rw)/sizeof(double);
      lpf=sizeof(pf)/sizeof(double);
      liw=sizeof(iw)/sizeof(long int);
      /* Print midaco headline and basic information */
      midaco_print(1,printeval,save2file,&iflag,&istop,&*f,&*g,&*x,&*xl,&*xu,
                 o,n,ni,m,me,&*rw,&*pf,maxeval,maxtime,&*param,p,&*key);
      while(istop==0) /*~~~ Start of the reverse communication loop ~~~*/
      {
          /* Evaluate objective function */
          problem_function( &*f, &*g, &*x, val);

          /* Call MIDACO */
          midaco(&p,&o,&n,&ni,&m,&me,&*x,&*f,&*g,&*xl,&*xu,&iflag,
                 &istop,&*param,&*rw,&lrw,&*iw,&liw,&*pf,&lpf,&*key);
          /* Call MIDACO printing routine */
          midaco_print(2,printeval,save2file,&iflag,&istop,&*f,&*g,&*x,&*xl,&*xu,
                       o,n,ni,m,me,&*rw,&*pf,maxeval,maxtime,&*param,p,&*key);
      } /*~~~End of the reverse communication loop ~~~*/
      /*****************************************************************/
//      printf("\n Solution f[0] = %f ", f[0]);
//      printf("\n Solution g[0] = %f ", g[0]);
//      printf("\n Solution x[0] = %f ", x[0]);
//      printf("\n Solution x[1] = %f ", x[1]);
        cout << "\n    a = " << x[0] << "\n    b = " << x[1] << "\n";
      /*****************************************************************/
      return 0;
}

int degeneracies(int x, ofstream& f) {
    int a = 0, b = 0, c = 0, degen = 0;
    vector <components> abc;
    while (pow(a, 2) <= x) {
        b = a;
        while (pow(b, 2) <= x) {
            c = b;
            while (pow(c, 2) <= x) {
                if (pow(a, 2) + pow(b, 2) + pow(c, 2) == x) {
                    degen++;
                    abc.push_back({a, b, c});
                }
            c++;
            }
        b++;
        }
    a++;
    }

    cout << "\n" << x << "\n  Degeneracy: " << degen << endl;
    f << "\n" << x << "\n  Degeneracy: " << degen << endl;

    if (degen == 0) {
        solve(x);
    }

    int s = abc.size();
    for (int i=0; i<s; i++)
    {
        // Accessing structure members using their names.
        f << "  " << abc[i].a << ", " << abc[i].b
             << ", " << abc[i].c << endl;
    } //end for
    abc.clear();
    return degen;
}

int main()
{
    time_t start, end;
    time(&start);

    int x = 1000; // Change ceiling here

    vector <int> n(x+1), d(x+1);

    ofstream f;
    // Output file control
    f.open("TS_cpp.txt", ios::out);

    for (int i = 1; i <= x; i++) {
            int degen = degeneracies(i, f);
            n.at(i) = i;
            d.at(i) = degen;
    } //end for

    plt::scatter(n, d);

    time(&end);
    double time_taken = double(end - start);

    cout << "Time taken by program is : " << fixed << time_taken;
    cout << " sec " << endl;

    plt::show();
}
