<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from './components/Navigation.svelte'
  import UserCreate from './routes/UserCreate.svelte'
  import UserLogin from './routes/UserLogin.svelte'
  import QuestionModify from "./routes/QuestionModify.svelte"
  import AnswerModify from "./routes/AnswerModify.svelte"

  const routes = {
    '/': Home,
    '/detail/:question_id': Detail,
    '/question-create': QuestionCreate,
    '/user-create': UserCreate,
    '/user-login': UserLogin,
    '/question-modify/:question_id': QuestionModify,
    '/answer-modify/:answer_id': AnswerModify,
  }
</script>

<Navigation />
<Router {routes}/>

<!--
<script>
  let question_list = []

  function get_question_list() {
    fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
      response.json().then((json) => {
        question_list = json
      })
    })
  }

  get_question_list()
</script>

<ul>
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>
-->

<!--
<h1>Hello</h1>
-->

<!--
<script>
  let message;

  fetch("http://127.0.0.1:8000/hello").then((response) => {
    response.json().then((json) => {
      message = json.message
    });
  });
</script>
-->

<!--
<script>
  async function hello() {
    const res = await fetch("http://localhost:8000/hello");
    const json = await res.json();

    if(res.ok){
      return json.message;
    }
    else{
      alert("error")
    }
  }

  let promise = hello();
</script>

 
async(비동기) 함수인 hello는 "promise(변수명)" 객체를 반환
1. Pending (대기 중): 아직 작업이 끝나지 않은 상태. fetch 요청을 보내고 서버로부터 응답을 기다리는 중
2. Fulfilled (성공): 작업이 성공적으로 완료된 상태. 서버로부터 응답(res)을 잘 받고, json.message 값을 성공적으로 반환했을 때
3. Rejected (실패): 작업이 실패한 상태. 네트워크 오류로 fetch가 실패하거나 서버가 에러를 응답했을 때

{#await promise}
  <p>...waiting</p>
{:then message}
  <h1>{message}</h1>
{/await}
-->>