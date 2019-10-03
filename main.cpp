

#include "Server.h"
#include "Client.h"

#include <iostream>
#include <set>
#include <sstream>
#include <string>

namespace
{
   /////////////////////////////////////////////////////////////////////////////
   ///
   ///   @brief  Get usage string
   ///
   /////////////////////////////////////////////////////////////////////////////
   std::string Help(const std::string& appname)
   {
      std::stringstream ss;
      ss << "usage: " << appname << " [options]" << "\n"
         << "   options:"                        << "\n"
         << "      -s, --server: run 1 server"   << "\n"
         << "      -c, --client [N]: run N clients (default 1)";
      return ss.str();
   }
   
} // end namespace


int main(int argc, char **argv)
{
   // Args to vector
   std::set<std::string> args;
   for (i = 1 ; i < argc ; ++i)
   {
      args.insert(argv[i]);
   }
   
   // No args?
   if (args.empty())
   {
      std::cerr << Help(argv[0]) << std::endl;
      return 1;
   }
   
   // Help arg?
   if (args.find("-h") != args.cend() || args.find("--help") != args.cend())
   {
      std::cout << Help(argv[0]) << std::endl;
      return 1;
   }
   
   // Random seed
   unsigned int seed = static_cast<unsigned int>(time(NULL));
   std::cerr << "srand(" << seed << ")" << std::endl;
   srand(seed);
   
   
   
   // Server?
   Server server;
   
   // Client(s)?
   Client client;
   
   return 0;
}

