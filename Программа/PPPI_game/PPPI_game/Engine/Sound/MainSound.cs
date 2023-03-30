using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// Перечисление популярных групп для проигрывания музыки
/// </summary>
public enum Groups
{
    /// <summary>
    /// Элемент перечисления, который указывает на группу AC/DC
    /// </summary>
    AC_DC,

    /// <summary>
    /// Элемент перечисления, который указывает на группу PinkFloyd
    /// </summary>
    Pink_Floyd,

    /// <summary>
    /// Элемент перечисления, который указывает на группу Aerosmith
    /// </summary>
    Aerosmith
}

namespace PPPI_game
{

    /// <summary>
    /// Воспроизведение музыки
    /// </summary>
    public class MainSound
    {
        /// <summary>
        /// Переменная для выбора популярных групп
        /// </summary>
        private Groups _groups; 

        /// <summary>
        /// Проиграть музыку
        /// </summary>
        public void PlayMusic()
        {
            _groups = Groups.Pink_Floyd;
        }
    }
}
