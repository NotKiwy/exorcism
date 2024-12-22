from setuptools import setup, find_packages
from setuptools.command.install import install
import os

def banner(text):
    lines = text.split('\n')
    grdtext = []

    for i, line in enumerate(lines):
        ratio = 1 - (i / len(lines))
        green = blue = int(255 * ratio)
        line = f"\033[38;2;255;{green};{blue}m{line}\033[0m"
        grdtext.append(line)

    return '\n'.join(grdtext)

MESSAGE = """                                                            .                                    
                                        .         ;                                    
           .              .              ;%     ;;                                     
             ,           ,                :;%  %;                                      
              :         ;                   :;%;'     .,                               
     ,.        %;     %;            ;        %;'    ,;                                
       ;       ;%;  %%;        ,     %;    ;%;    ,%'                                 
        %;       %;%;      ,  ;       %;  ;%;   ,%;'          ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓██████████████▓▒░
         ;%;      %;        ;%;        % ;%;  ,%;'            ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
          `%;.     ;%;     %;'         `;%%;.%;'              ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
           `:;%.    ;%%. %@;        %; ;@%;%'                 ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
              `:%;.  :;bd%;          %;@%;'                   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
                `@%:.  :;%.         ;@@%;'                    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
                  `@%.  `;@%.      ;@@%;                      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
                    `@%%. `@%%    ;@@%;                                              
                     ;@%. :@%%  %@@%;                                        ╔════════════════════════════════════════════════════════════════════╗
                       %@bd%%%bd%%:;                                         ║                          EXORCISM INFORMATION                      ║
                         #@%%%%%:;;                                          ║                                                                    ║
                         %@@%%%::;                                           ║    NAME >> Exorcism                                                ║
                         %@@@%(o);  . '                                      ║    VERSION >> 1.0.0                                                ║
                         %@@@o%;:(.,'                                        ║    DEVELOPER >> notkiwy                                            ║
                     `.. %@@@o%::;                                           ║    SUPPORT >> notkiwy@yahoo.com                                    ║
                        `)@@@o%::;                                           ║    GITHUB >> https://github.com/notkiwy/exorcism                   ║
                         %@@(o)::;                                           ║    PYTHON REQUIRED >> >=3.6                                        ║
                        .%@@@@%::;                                           ╚════════════════════════════════════════════════════════════════════╝
                        ;%@@@@%::;.                          
                       ;%@@@@%%:;;;.                        
                   ...;%@@@@@%%:;;;;,..                     
                                                                               
                                                                            
                                                                            
"""

class Install(install):
    def run(self):
        install.run(self)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner(MESSAGE))


setup(
    name="exorcism",
    version="1.0.0",
    author="notkiwy",
    author_email="notkiwy@yahoo.com",
    description=">.<",
    packages=find_packages(),
    python_requires=">=3.6",
    cmdclass={
        'install': Install,
    },
)
