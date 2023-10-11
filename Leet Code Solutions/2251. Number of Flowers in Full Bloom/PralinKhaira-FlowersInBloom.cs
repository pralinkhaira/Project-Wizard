public class Solution {
    public int[] FullBloomFlowers(int[][] flowers, int[] people) 
    {
        var n = people.Length;
        var result = new int[n];
        var events = new Dictionary<int, int> ();
        foreach(var flower in flowers)
        {
            events.TryAdd(flower[0], 0);
            events[flower[0]] += 1;

            events.TryAdd(flower[1] + 1, 0);
            events[flower[1] + 1] -= 1;
        }

        var keys = events.Keys.ToList();
        var sum = 0;
        keys.Sort();
        foreach(var key in keys)
        {
            events[key] += sum;
            sum = events[key];
        }

        for(int i = 0; i < n; ++i)
        {
            var person = people[i];

            var left = 0;
            var right = keys.Count() - 1;
            var recent = -1;

            while(left <= right)
            {
                var temp = left + (right - left)/2;

                if(keys[temp] <= person)
                {
                    recent = keys[temp];
                    left = temp + 1;
                }
                else
                {
                    right = temp - 1;
                }
            }

            result[i] = recent == -1 ? 0 : events[recent];
        }

        return result;
    }
}