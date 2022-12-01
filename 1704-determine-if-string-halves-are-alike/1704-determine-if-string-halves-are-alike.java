class Solution {
    public boolean halvesAreAlike(String s) {
        int c1 = 0, c2 = 0;
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(Character.toLowerCase(s.charAt(i)))) {
                if (i < s.length()/2) {
                    c1++;
                }
                else{
                    c2++;
                }
            } 
        }
        
        if (c1 == c2) {
            return true;
        }
        return false;
    }
}