

#pragma once

// forward declarations
class Getter;
class Handler;
class Talker;


////////////////////////////////////////////////////////////////////////////////
///
///   @brief  
///
////////////////////////////////////////////////////////////////////////////////
class Client
{
public:
   Client(Getter* pGetter, Handler* pHandler, Talker* pTalker);
   virtual ~Client();
   
   void DFS();
   
private:
   Client(const Client&) = delete;
   Client& operator=(const Client&) = delete;
   
   Getter*  m_pGetter;  ///< Retrieve nodes / edges
   Handler* m_pHandler; ///< Handle retrieved nodes / edges
   Talker*  m_pTalker;  ///< Talk to server / other clients
};

