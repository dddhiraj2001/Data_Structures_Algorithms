def sumofdigits(n):
    if n//10==0:
        return n
    else:
        return n%10+sumofdigits(n//10)

print(sumofdigits(20166612937129837982173091238742199234762746296437562946527626947562784659826457629783564897263945692382369826495624352946589264756928346592368972364578326897265823841234862874623648168976418764164781638641879634871687641876896176161698676487164136461278469837467167613745156471567846198648168741684617864871632874631874617263423146187361764361384618972364186287461238461768716237613264135461521461864871684618726176716874612746876328942))