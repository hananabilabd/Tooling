import os, sys
from datetime import date

NAME = "Mohammad Mohsen"

HELP =  "This script makes a new folder and files for given modules\n"+\
        "Usage: module_make.py module_1 [module_2, ...]"

def main(path,*args):
  
  if len(args) < 0:
    
    raise(ValueError, "No arguments!")
    print(HELP)
  
  else:
    print(path)
    parent_dir = os.getcwd()

    for module in args:
      module = path +module
      #os.mkdir(module)
      #os.chdir(module)
      
      ## Program file
      with open(module+"_program.c", "w") as prog:
        
        prog.write("/*******************************************************************************\n")
        prog.write("* File    : "+module+"_program.c\n")
        prog.write("* Author  : "+NAME+"\n")
        prog.write("* Version : 1.0\n")
        prog.write("* Date    : "+str(date.today().day)+"/"+str(date.today().month)+"/"+str(date.today().year)+"\n")
        prog.write("*******************************************************************************/\n")
        prog.write("/*******************************************************************************\n")
        prog.write("* Description  :\n")
        prog.write("*******************************************************************************/\n")
        prog.write("\n\n")
        prog.write("#include <"+module+"_interface.h>\n")
        prog.write("#include <"+module+"_private.h>\n")
        prog.write("#include <"+module+"_config.h>\n")
        prog.write("\n\n")
        
    
      ## Interface file
      with open(module+"_interface.h", "w") as inter:
        
        inter.write("/*******************************************************************************\n");
        inter.write("* File    : "+module+"_interface.h\n")
        inter.write("* Author  : "+NAME+"\n")
        inter.write("* Version : 1.0\n")
        inter.write("* Date    : "+str(date.today().day)+"/"+str(date.today().month)+"/"+str(date.today().year)+"\n")
        inter.write("*******************************************************************************/\n");
        inter.write("/*******************************************************************************\n");
        inter.write("* Description  :\n")
        inter.write("*******************************************************************************/\n");
        inter.write("\n\n")
        inter.write("#ifndef _"+module+"_INTERFACE_H_\n")
        inter.write("#define _"+module+"_INTERFACE_H_\n")
        inter.write("\n\n")
        inter.write("#endif")
        inter.write("\n\n")
      
      ## Private file
      with open(module+"_private.h", "w") as prv:
        
        prv.write("/*******************************************************************************\n")
        prv.write("* File    : "+module+"_private.h\n")
        prv.write("* Author  : "+NAME+"\n")
        prv.write("* Version : 1.0\n");
        prv.write("* Date    : "+str(date.today().day)+"/"+str(date.today().month)+"/"+str(date.today().year)+"\n")
        prv.write("*******************************************************************************/\n")
        prv.write("/*******************************************************************************\n")
        prv.write("* Description  :\n")
        prv.write("*******************************************************************************/\n")
        prv.write("\n\n")
        prv.write("#ifndef _"+module+"_PRIVATE_H_\n")
        prv.write("#define _"+module+"_PRIVATE_H_\n")
        prv.write("\n\n")
        prv.write("#endif")
        prv.write("\n\n")
        
      ## Config file
      with open(module+"_config.h", "w") as conf:
        
        conf.write("/*******************************************************************************\n")
        conf.write("* File    : "+module+"_config.h\n")
        conf.write("* Author  : "+NAME+"\n")
        conf.write("* Version : 1.0\n");
        conf.write("* Date    : "+str(date.today().day)+"/"+str(date.today().month)+"/"+str(date.today().year)+"\n")
        conf.write("*******************************************************************************/\n")
        conf.write("/*******************************************************************************\n")
        conf.write("* Description  :\n")
        conf.write("*******************************************************************************/\n")
        conf.write("\n\n")
        conf.write("#ifndef _"+module+"_CONFIG_H_\n")
        conf.write("#define _"+module+"_CONFIG_H_\n")
        conf.write("\n\n")
        conf.write("#endif")
        conf.write("\n\n")
      
      os.chdir(parent_dir)
      
if __name__ == '__main__':
  main()

