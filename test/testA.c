// ***
// *** Please modify this file and check what would happen
// ***

#include <stdio.h>   // declare functions for input and output
#include <stdlib.h>  // define EXIT_FAILURE and EXIT_SUCCESS
#include <string.h>  // for strcmp
#include <stdbool.h> // for Boolean type (true or false)
// For header files provided by C, use < >
// gcc looks for these header files in /usr/include

#ifdef TEST_MAIN
int main(int argc, char * * argv)
{
  if (argc != 4)
    {
      fprintf(stderr, "argc is %d, not 4\n", argc);
      // stderr means standard error, usually it is the computer
      // screen but it is possible to save the messages to a file
      // by using ">&" (without the quotation marks)
      
      return EXIT_FAILURE;
      // Since the program cannot do what it needs to do (add,
      // subtract, multiply, or divide), it returns EXIT_FAILURE.
      // Use EXIT_FAILURE or EXIT_SUCCESS
      // Do NOT use return 0, -1, or 1
    }
  
  // Truncated since not everything is needed
  return EXIT_SUCCESS;
}

#endif
