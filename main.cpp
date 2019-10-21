

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
   
   /////////////////////////////////////////////////////////////////////////////
   ///
   ///   @brief  Wait for the user to quit
   ///
   /////////////////////////////////////////////////////////////////////////////
   void Block()
   {
      std::cout << "Press any key to quit." << std::endl;
      
      char whatever;
      std::cin >> whatever;
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
   
   bool valid  = !args.empty();
   bool help   = args.erase("-h") != args.cend() || args.erase("--help")   != args.cend();
   bool server = args.erase("-s") != args.cend() || args.erase("--server") != args.cend();
   bool client = args.erase("-c") != args.cend() || args.erase("--client") != args.cend();
   valid = valid && (server || client);
   
   // Optional number of clients
   int nClients = 1;
   if (client && args.size() == 1)
   {
      nClients = std::stoi(*args.begin());
      args.erase(args.begin())
   }
   
   // Help arg?
   if (!valid)
   {
      std::cout << Help(argv[0]) << std::endl;
      return 1;
   }
   
   // No args?
   if (help)
   {
      std::cerr << Help(argv[0]) << std::endl;
      return 1;
   }
   
   // Random seed
   unsigned int seed = static_cast<unsigned int>(time(NULL));
   std::cerr << "srand(" << seed << ")" << std::endl;
   srand(seed);
   
   if (server && client) // Both
   {
      for (int i = 0 ; i < nClients ; ++i) { Client client; }
      Server server;
   }
   else if (server) // Server
   {
      Server server;
   }
   else if (client) // Client(s)
   {
      for (int i = 0 ; i < nClients ; ++i) { Client client; }
   }
   
   Block();
   return 0;
}

