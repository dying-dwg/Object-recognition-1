# Object recognition and determination of its Cartesian coordinates in the image by calculating the mutual correlation function in the space-time domain
Translate the resulting images from standard graphic format files into two-dimensional arrays of pixels suitable for computer processing (using Intel OpenCV)
Calculate the cross-correlation functions of the image under study with each of the desired (reference) as functions of their mutual displacements along Cartesian coordinate axes. Determine by the type of calculated correlation functions (correlation fields) which of the desired objects is present in the original image and what is its position in it. Estimate the calculation time of the correlation field as a function of the linear dimensions of the matched images. The calculation of the cross-correlation functions should be performed without the use of the fast Fourier transform (FFT). The calculated correlation field is visualized by displaying it in a graphical window on the terminal screen, or by writing it to a file of a standard graphical format.

### Example of work
> Main Image and desired image

<img src="https://cdn.discordapp.com/attachments/986664884194377728/1035229986619129947/unknown.png" width="600">     <img src="https://cdn.discordapp.com/attachments/986664884194377728/1035230031577882696/unknown.png" width="100">
> Result
<img src="https://cdn.discordapp.com/attachments/986664884194377728/1035230554020384869/unknown.png" width="600">

### Using libraries
- cv2 - OpenCV used to search for an image (Template Matching)
- time - To count the working hours
- numpy - For working with arrays
- matplotlib (pyplot) - To create and output graphs
- os - To get a list of files in a directory.
____

# Распознавание объекта и определение его декартовых координат на изображении путем вычисления функции взаимной корреляции в пространственно-временной области
Перевести полученные изображения, из файлов стандартного графического формата в двумерные массивы пикселов, пригодные для компьютерной обработки (используя Intel OpenCV)
Вычислить взаимные корреляционные функции исследуемого изображения с каждым из искомых (эталонных) как функции их взаимных смещений вдоль декартовых координатных осей. Определить по виду вычисленных корреляционных функций (корреляционных полей), какой из искомых объектов присутствует в исходном изображении и какова его позиция в нем. Оценить время вычисления корреляционного поля как функцию линейных размеров сопоставляемых изображений. Вычисление функций взаимной корреляции производить без применения быстрого преобразования Фурье (БПФ). Визуализацию рассчитанного корреляционного поля производить путем вывода его в графическое окно на экране терминала, или путем его записи в файл стандартного графического формата.
