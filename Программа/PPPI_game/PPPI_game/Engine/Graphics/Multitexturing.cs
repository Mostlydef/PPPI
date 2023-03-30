using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace PPPI_game
{
    /// <summary>
    /// Класс отвечающий за рендеринг с использованием нескольких текстур за минимальное число проходов
    /// </summary>
    public class Multitexturing
    {

        /// <summary>
        /// Операции изменения позиции, размера, или ориентации объекта в пространстве.
        /// </summary>
        public void Transforms()
        {

        }

        /// <summary>
        /// Операции подобные превращениям, однако, более сложные,
        /// так как их исполнение приводят к перемене внешнего вида объекта.
        /// </summary>
        public void Deforms()
        {

        }

        /// <summary>
        /// Отсечение тех многоугольников, которые не попадают в поле зрения пользователя.
        /// </summary>
        public void Clipping()
        {

        }

        /// <summary>
        /// Распределение, (иначе - распределение текстур, Texture Mapping)
        ///  - процесс назначения объекту атрибутов придающих ему реалистичность.
        /// </summary>
        public void Mapping()
        {

        }

        /// <summary>
        /// Механизм получения изображения в HiColor-режимах.
        /// </summary>
        public void Dithering()
        {

        }
    }
}
