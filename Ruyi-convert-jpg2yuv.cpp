#include <opencv/highgui.h>
#include <opencv/cv.h>
#include <opencv2/imgproc/imgproc_c.h>

using namespace cv;

int main(int argv, char **argc)
{
	IplImage *pstImage = NULL;
	IplImage *pstYUVImage = NULL;
	FILE *fp = NULL;

	pstImage = cvLoadImage("C://Users/Administrator/Desktop/abc/FaceNew/5.jpg", CV_LOAD_IMAGE_COLOR);
	fp = fopen("C://Users/Administrator/Desktop/abc/FaceNew/5.yuv", "wb");
	pstYUVImage = cvCreateImage(cvSize(pstImage->width, pstImage->height), IPL_DEPTH_8U, 3);

	cvCvtColor(pstImage, pstYUVImage, CV_BGR2YUV);

	for (int i = 0; i < pstImage->width * pstImage->height; i++)
	{
		//提取Y分量
		fwrite(&pstYUVImage->imageData[i * 3], 1, 1, fp);
		//提取U分量
		//fwrite(&pstYUVImage->imageData[i*3+2], 1 , 1, fp);
		//提取V分量
		//fwrite(&pstYUVImage->imageData[i*3+1], 1 , 1, fp);
	}

	for (int i = 0; i < pstImage->height; i = i + 2)
	{
		for (int j = 0; j < pstImage->width; j = j + 2)
		{
			//提取U分量
			fwrite(&pstYUVImage->imageData[3 * (i*pstImage->width + j) + 2], 1, 1, fp);
		}
	}

	for (int i = 0; i < pstImage->height; i = i + 2)
	{
		for (int j = 0; j < pstImage->width; j = j + 2)
		{
			//提取V分量
			fwrite(&pstYUVImage->imageData[3 * (i*pstImage->width + j) + 1], 1, 1, fp);
		}
	}

	cvShowImage("Win", pstImage);

	cvWaitKey(0);
	cvReleaseImage(&pstImage);
	cvReleaseImage(&pstYUVImage);
	fclose(fp);
	return 0;
