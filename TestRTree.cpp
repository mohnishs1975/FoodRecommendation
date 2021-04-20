//
// Test.cpp
//
// This is a direct port of the C version of the RTree test program.
//

#include <stdio.h>
#include "RTree.h"

struct Rect
{
  Rect()  {}

  Rect(float a_minX, float a_minY)
  {
    min[0] = a_minX;
    min[1] = a_minY;

    max[0] = a_minX + .01;
    max[1] = a_minY + .01;
  }


  float min[2];
  float max[2];
};

struct Point
{
  Point(){}
  Point(float _x, float _y){
    x = _x;
    y = _y;
  }
  float x;
  float y;
};

struct Rect rects[] = 
{
Rect(42.0,-71.0), //BU
Rect(41.0,-72.0), //Photonics
Rect(43.0,-73.0),//Law
//Test point 
//NY's lot 
Rect(15.0,-20.0),//Times Square
Rect(16.0,-22.0),//Madam Tussade
Rect(13.0,-21.0),//
};

struct Point points[] = 
{
Point(42.3504997,-71.1075878), //BU
Point(42.3510452,-71.1071438), //Photonics
Point(42.3505067,-71.1077229),//Law
//Test point 
//NY's lot 
Point(40.7579747,-73.9877313),//Times Square
Point(40.757406,-73.99136),//Madam Tussade
Point(40.7504824,-74.0189432),//
};


int nrects = sizeof(rects) / sizeof(rects[0]);

//Rect search_rect(40.7515149,-74.0052236); // search will find above rects that this one overlaps
//Empire State 

//Rect search_rect(42.3466661,-71.1042568); //Boston search

Rect search_rect(41.0,-72.0); 
bool MySearchCallback(int id, void* arg) 
{
  printf("Hit data rect %d\n", id);
  return true; // keep going
}


int main()
{
  RTree<int, float, 2> tree;

  int i, nhits;
  printf("nrects = %d\n", nrects);

  for(i=0; i<nrects; i++)
  {
    tree.Insert(rects[i].min, rects[i].max, i); // Note, all values including zero are fine in this version
  }

  nhits = tree.Search(search_rect.min, search_rect.max, MySearchCallback, NULL);

  printf("Search resulted in %d hits\n", nhits);

  // Iterator test 
  int itIndex = 0;
  RTree<int, float, 2>::Iterator it;
  for( tree.GetFirst(it); 
       !tree.IsNull(it);
       tree.GetNext(it) )
  {
    int value = tree.GetAt(it);
    
    float boundsMin[2] = {0.0,0.0};
    float boundsMax[2] = {0.0,0.0};
    it.GetBounds(boundsMin, boundsMax);
    printf("it[%d] %d = (%d,%d,%d,%d)\n", itIndex++, value, boundsMin[0], boundsMin[1], boundsMax[0], boundsMax[1]);
  }
  
  // Iterator test, alternate syntax
  itIndex = 0;
  tree.GetFirst(it);
  while( !it.IsNull() )
  {
    int value = *it;
    ++it;
    printf("it[%d] %d\n", itIndex++, value);
  }

  getchar(); // Wait for keypress on exit so we can read console output

// Output
// nrects = 6
// Hit data rect 1
// Search resulted in 1 hits
// it[0] 0 = (0,1078263808,0,-1068384256)
// it[1] 1 = (0,1078231040,0,-1068367872)
// it[2] 2 = (0,1078296576,0,-1068351488)
// it[3] 3 = (0,1076756480,0,-1070333952)
// it[4] 4 = (0,1076887552,0,-1070202880)
// it[5] 5 = (0,1076494336,0,-1070268416)
// it[0] 0
// it[1] 1
// it[2] 2
// it[3] 3
// it[4] 4
// it[5] 5

return 0;
}
