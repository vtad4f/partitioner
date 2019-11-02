

#pragma once

// forward declarations
class Graph;
class Node;

////////////////////////////////////////////////////////////////////////////////
///
///   @brief  
///
////////////////////////////////////////////////////////////////////////////////
class Getter
{
public:
   Getter();
   virtual ~Getter();
   
   void Set(Graph* pGraph);
   void Set(Node* pNode);
   
   Node* Current() const;
   bool Next();
   
private:
   Getter(const Getter&) = delete;
   Getter& operator=(const Getter&) = delete;
   
   Graph* m_pGraph;
   Node* m_pCurrent;
};

