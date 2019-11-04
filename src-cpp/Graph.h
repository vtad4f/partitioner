

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
   static void Parse(Graph* pGraph, const char* filePath, uint64_t limit = 0, uint64_t offset = 0);
   bool Claim(const std::string& nodeID);
   
private:
   Graph(const Graph&) = delete;
   Graph& operator=(const Graph&) = delete;
   
   std::atomic<std::vector<bool> > m_Claimed;
   std::map<std::string, uint64_t> m_NodeIDs; // TODO - std:unordered_map ?
};

