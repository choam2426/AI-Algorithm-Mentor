# AI-Algorithm-Mentor
### OPENAI의 언어 모델을 사용해서 알고리즘 문제에 대한 피드백을 제공합니다.
백준, 프로그래머스 등을 통해 알고리즘 공부를 하시는 분들에게 도움을 주기 위해 만들었습니다.  
코딩 테스트 준비, 알고리즘 공부 등 학습에 큰 도움을 줄 수 있습니다. **특히 독학을 하신다면...**  
**본 프로젝트는 오픈 소스 프로젝트로 많은 참여와 조언을 환영합니다.**

## 사용 결과
[개발자의 리포지토리](https://github.com/choam2426/OnlineJudge)  
실제로 본 프로젝트를 사용하고 있는 리포지토리입니다. 커밋 기록을 확인해보세요~ 

## 사용 방법
본 프로젝트는 크롬 익스텐션 [<U>백준 허브</U>](https://github.com/BaekjoonHub/BaekjoonHub) 사용을 전제로 만들어졌습니다. **백준 허브** 사용을 권장합니다.  
(백준 허브는 문제 내용도 같이 올려줘서 더 좋은 피드백을 받을 수 있습니다.)  
아래 내용은 모두 **백준 허브**를 연동한 github repository에서 이루어집니다.

### 1. OPENAI API Key 등록하기
[<U>OPENAI API</U>](https://openai.com/index/openai-api/)에서 API 사용을 위한 KEY를 생성하고 credit을 결제합니다. (한 문제 당 0.01$ 내외로 비용이 사용됩니다.)  
생성한 키를 **백준 허브**와 연동한 repository에 "**OPENAI_API_KEY**"를 이름으로 secrets에 등록합니다.

### 2. github action 등록하기
github action에 다음 workflow를 추가합니다.
```
name: AI algorithm mentor

on:
  push:
    branches: [ "main" ]

jobs:
  write_comment:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: choam2426/AI-Algorithm-Mentor@v3
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }} # OPENAI API 크레딧 필요
```
🚩 GITHUB_TOKEN은 따로 Secrets에 등록하지 않으셔도 됩니다.

### 3. 문제 풀기
이제 문제를 풀고 백준 허브가 자동으로 push를 하면 해당 커밋에 comment가 생성됩니다.
