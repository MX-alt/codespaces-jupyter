#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

TreeNode* buildBST(const vector<int>& nums, int lo, int hi) {
    if (lo > hi) return nullptr;
    int mid = lo + (hi - lo) / 2;
    TreeNode* node = new TreeNode(nums[mid]);
    node->left = buildBST(nums, lo, mid - 1);
    node->right = buildBST(nums, mid + 1, hi);
    return node;
}

TreeNode* sortedArrayToBST(const vector<int>& nums) {
    return buildBST(nums, 0, static_cast<int>(nums.size()) - 1);
}

bool isValidBST(TreeNode* node, long lo, long hi) {
    if (node == nullptr) return true;
    if (node->val <= lo || node->val >= hi) return false;
    return isValidBST(node->left, lo, node->val) && isValidBST(node->right, node->val, hi);
}

int height(TreeNode* node) {
    if (node == nullptr) return 0;
    return 1 + max(height(node->left), height(node->right));
}

bool isHeightBalanced(TreeNode* node) {
    if (node == nullptr) return true;
    return abs(height(node->left) - height(node->right)) <= 1
        && isHeightBalanced(node->left)
        && isHeightBalanced(node->right);
}

vector<int> inorder(TreeNode* node) {
    if (node == nullptr) return {};
    vector<int> result;
    vector<int> leftVals = inorder(node->left);
    result.insert(result.end(), leftVals.begin(), leftVals.end());
    result.push_back(node->val);
    vector<int> rightVals = inorder(node->right);
    result.insert(result.end(), rightVals.begin(), rightVals.end());
    return result;
}

void deleteTree(TreeNode* node) {
    if (node == nullptr) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

int main() {
    TreeNode* t = sortedArrayToBST({});
    assert(t == nullptr);

    t = sortedArrayToBST({1});
    assert(t->val == 1 && t->left == nullptr && t->right == nullptr);
    deleteTree(t);

    t = sortedArrayToBST({-10, -3, 0, 5, 9});
    assert(inorder(t) == vector<int>({-10, -3, 0, 5, 9}));
    assert(isValidBST(t, numeric_limits<long>::min(), numeric_limits<long>::max()));
    assert(isHeightBalanced(t));
    deleteTree(t);

    t = sortedArrayToBST({1, 2, 3, 4});
    assert(inorder(t) == vector<int>({1, 2, 3, 4}));
    assert(isValidBST(t, numeric_limits<long>::min(), numeric_limits<long>::max()));
    assert(isHeightBalanced(t));
    deleteTree(t);

    vector<int> nums(15);
    for (int i = 0; i < 15; i++) {
        nums[i] = i + 1;
    }
    t = sortedArrayToBST(nums);
    vector<int> expected(15);
    for (int i = 0; i < 15; i++) {
        expected[i] = i + 1;
    }
    assert(inorder(t) == expected);
    assert(isValidBST(t, numeric_limits<long>::min(), numeric_limits<long>::max()));
    assert(isHeightBalanced(t));
    deleteTree(t);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
