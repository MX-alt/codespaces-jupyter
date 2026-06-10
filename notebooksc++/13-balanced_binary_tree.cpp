#include <cassert>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

int checkHeight(TreeNode* node) {
    if (node == nullptr) return 0;

    int leftHeight = checkHeight(node->left);
    if (leftHeight == -1) return -1;

    int rightHeight = checkHeight(node->right);
    if (rightHeight == -1) return -1;

    if (abs(leftHeight - rightHeight) > 1) return -1;
    return 1 + max(leftHeight, rightHeight);
}

bool isBalanced(TreeNode* root) {
    return checkHeight(root) != -1;
}

TreeNode* buildTree(const vector<int>& vals) {
    if (vals.empty() || vals[0] == INT_MIN) return nullptr;

    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;

    while (!q.empty() && i < static_cast<int>(vals.size())) {
        TreeNode* node = q.front();
        q.pop();

        if (i < static_cast<int>(vals.size()) && vals[i] != INT_MIN) {
            node->left = new TreeNode(vals[i]);
            q.push(node->left);
        }
        i++;

        if (i < static_cast<int>(vals.size()) && vals[i] != INT_MIN) {
            node->right = new TreeNode(vals[i]);
            q.push(node->right);
        }
        i++;
    }

    return root;
}

void deleteTree(TreeNode* node) {
    if (node == nullptr) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

int main() {
    assert(isBalanced(nullptr) == true);

    TreeNode* single = buildTree({1});
    assert(isBalanced(single) == true);
    deleteTree(single);

    TreeNode* balanced = buildTree({3, 9, 20, INT_MIN, INT_MIN, 15, 7});
    assert(isBalanced(balanced) == true);
    deleteTree(balanced);

    TreeNode* unbalanced = buildTree({1, 2, 2, 3, 3, INT_MIN, INT_MIN, 4, 4});
    assert(isBalanced(unbalanced) == false);
    deleteTree(unbalanced);

    TreeNode* skewed = new TreeNode(1, nullptr, new TreeNode(2, nullptr, new TreeNode(3)));
    assert(isBalanced(skewed) == false);
    deleteTree(skewed);

    cout << "All test cases passed ✅" << endl;
    return 0;
}
