﻿/*

Высота бассейна всегда ограничена меньшей палкой — вода выше просто выльется через неё.
Если хотим больше площадь, нам нужно либо шире расстояние (но мы уже на максимальном расстоянии, ведь взяли самую левую и правую), либо выше минимум палок.

Картинка в голове
Представьте: если крайняя левая палка низкая, сколько бы ни двигали правую внутрь (делали бассейн уже), уровень воды будет ограничен всё той же низкой палкой. Никогда не выжмем больший объём, пока не попробуем что-то выше слева.
То есть мы ничего не теряем — любые комбинации с текущей низкой палкой и более «узким» бассейном попробованы уже, когда указатели стояли шире.

*/

// 4. Container With Most Water
var heights = new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
Console.WriteLine(MaxArea(heights));

/*
          █                   █        
          █                   █       █
          █   █               █       █
          █   █       █       █       █
          █   █       █   █   █       █
          █   █       █   █   █   █   █
      █   █   █   █   █   █   █   █   █
      █   █   █   █   █   █   █   █   █
      0   1   2   3   4   5   6   7   8

// Максимальный контейнер между индексами 1 (8) и 8 (7)
// Площадь: min(8,7)*(8-1) = 49

*/

int MaxArea(int[] height)
{
    int left = 0, right = height.Length - 1;
    int maxArea = 0;
    while (left < right)
    {
        int area = Math.Min(height[left], height[right]) * (right - left);
        maxArea = Math.Max(maxArea, area);
        if (height[left] < height[right])
            left++;
        else
            right--;
    }
    return maxArea;
}