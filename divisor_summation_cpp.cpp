#include <iostream>

int main()
{

	int testcase;
	std::cin >> testcase;
	for(int i = 0; i < testcase; i++)
	{
		int n; 
		std::cin >> n;
		int sum_val = 0;
		for (int j = 1; j*2 <= n; j++)
		{
			if (n % j == 0)	
			{
				sum_val = sum_val + j;
			}
		}
		std::cout << sum_val << std::endl;
	}
}
