#include <iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
	
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	int carry = 0;
	ListNode* res;
	while(true) {
		if(l1 != NULL && l2 != NULL) {
			int cur = (l1->val + l2->val + carry) % 10;
			res->val = cur;
			res = res->next;
			carry = (l1->val + l2->val + carry) / 10;
			l1 = l1->next;
			l2 = l2->next;
		}
		else if(l1 == NULL && l2 != NULL) {
			int cur = (l2->val + carry) % 10;
			res->val = cur;
			res = res->next;
			carry = (l2->val + carry) / 10;
			l2 = l2->next;
		}
		else if(l2 == NULL && l1 != NULL) {
			int cur = (l1->val + carry) % 10;
			res->val = cur;
			res = res->next;
			carry = (l1->val + carry) / 10;
			l1 = l1->next;
		}
		else if(l2 == NULL && l1 == NULL) {
			res->next = NULL;
			break;
		}
	}  
	return res;
}

int main() {
	ListNode* l1;
	l1->val = 0;
	l1->next = NULL;
	ListNode* l2;
	l2->val = 0;
	l2->next = NULL;
	ListNode* res = addTwoNumbers(l1, l2);
	cout << res->val << endl;
	return 0;
}
