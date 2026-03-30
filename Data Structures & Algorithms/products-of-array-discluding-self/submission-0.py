class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        precursors = [1]
        postcursors = [1]
        pre_prod = 1
        post_prod = 1

        for i in range(len(nums)-1):
            pre_prod *= nums[i]
            post_prod *= nums[-(i+1)]

            precursors.append(pre_prod)
            postcursors.append(post_prod)

        print(precursors)
        print(postcursors)

        output = []
        for i in range(len(precursors)):
            output.append(precursors[i] * postcursors[-(i+1)])
            # 1: pre[nothing] * post[2]
            # 2: pre[0] * post[1]
            # 3: pre[1] * post[0]
            # 4: pre[2] * post[nothing]

        return output