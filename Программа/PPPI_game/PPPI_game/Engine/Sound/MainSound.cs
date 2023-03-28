using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public enum Groups
{
    AC_DC,
    Pink_Floyd,
    Aerosmith
}

namespace PPPI_game.Engine.Sound
{

    internal class MainSound
    {
        Groups _groups; 
        // Проиграть музыку
        public void PlayMusic()
        {
            _groups = Groups.Aerosmith;
        }
    }
}
