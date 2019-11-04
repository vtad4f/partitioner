

#pragma once

// forward declarations
class Graph;


////////////////////////////////////////////////////////////////////////////////
///
///   @brief  
///
////////////////////////////////////////////////////////////////////////////////
class Client
{
public:
   Client(Graph* pGraph);
   virtual ~Client();
   
private:
   Client(const Client&) = delete;
   Client& operator=(const Client&) = delete;
   
   Graph* m_pGraph;
};

