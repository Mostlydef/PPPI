using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PPPI_game.Game
{
    internal abstract class Run_sNRoses
    {
        private int _damage;
        private int _rate;
        private int _distance;
        private int _magazine;

        public Run_sNRoses(int damage, int rate, int distance, int magazine)
        {
            _damage = damage;
            _rate = rate;
            _distance = distance;
            _magazine = magazine;
        }

        // Метод стрельбы
        public void Shoot()
        {

        }
    }
}
