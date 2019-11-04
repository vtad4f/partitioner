

#pragma once
#include <vector>
#include <string>


////////////////////////////////////////////////////////////////////////////////
///
///   @brief  
///
////////////////////////////////////////////////////////////////////////////////
class Graph
{
public:
   Graph(const char* filePath, uint64_t limit = 0, uint64_t offset = 0);
   virtual ~Graph();
   
   bool Claim(const std::string& nodeID);
   
private:
   Graph(const Graph&) = delete;
   Graph& operator=(const Graph&) = delete;
   
   std::atomic<std::vector<bool> > m_Claimed;
   /* const */ std::map<std::string, uint64_t> m_NodeIDs; // TODO - std:unordered_map ?
};

