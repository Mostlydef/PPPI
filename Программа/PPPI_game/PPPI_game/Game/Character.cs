using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PPPI_game.Game
{
    internal abstract class Character
    {
        private int _HP;
        private int _STP;
        private int _movementSpeed;

        public Character(int HP, int STP, int movementSpeed)
        {
            _HP = HP;
            _STP = STP;
            _movementSpeed = movementSpeed;
        }

        // Бег персонажа.
        public void Run()
        {

        }

        // Прижок.
        public void Jump()
        {

        }

        // Ускоренный бег.
        public void Accelerate()
        {

        }

        // Приседание.
        public void Squat()
        {

        }
    }
}
