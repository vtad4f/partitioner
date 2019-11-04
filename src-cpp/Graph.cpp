

#include "Graph.h"


////////////////////////////////////////////////////////////////////////////////
///
///   @brief  Populate the graph from the file
///
///   @param limit  Limit the number of lines read from the file
///   @param offset  Start at this line in the file
///
////////////////////////////////////////////////////////////////////////////////
void Graph::Parse(Graph* pGraph, const char* filePath, uint64_t limit, uint64_t offset)
{
   std::ifstream ifs(filePath);
   if (ifs && ifs.is_open())
   {
      std::string line;
      while (std::getline(ifs, line))
      {
         pGraph->m_NodeIDs.push_back();
      }
      pGraph->m_Claimed.resize();
   }
}


////////////////////////////////////////////////////////////////////////////////
///
///   @brief  
///
////////////////////////////////////////////////////////////////////////////////
bool Graph::Claim(const std::string& nodeID)
{
   return false;
}

