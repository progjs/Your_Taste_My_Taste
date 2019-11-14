# Your_Taste_My_Taste

## Task List

19-11-14 회의

목표 설정(19.11.14) Due date : 19.11.29 까지
	1. 모바일 환경에 적합하게 UI를 재설계하는거
	2. 위치기반 서비스
		페이지 상에서 접속 위치를 좌표 전달
		카카오맵 페이지 상에서 띄우기		
	3. 친구 찾고 등록하고 같이 먹기
		친구 페이지
		Ajax로 친구 CRUD 동기화
	4. DB 완성
		이미지 크롤링
		음식 정보
	5. 좋아요 기능에 따른 history DB update
	

니맛 내맛 개인 프로필 생성 작업
	
	-프로필 요소 검토 후 각 프로필요소 Create Update Read 기능
	
	-프론트 페이지 수정
		1. 종교, 채식주의 페이지 선택 가능하도록 form 수정
		2. allergy 페이지 form url 수정
		3. 개인 식성(hatelist 페이지) 자동완성 가능하도록 페이지에 음식, 재료정보 넘기기
		4. findinfo, findid 페이지에서 마이페이지로 이동해서는 안됨, 해당 '마이페이지' 글자 없에기
		
	-프론트 싫어하는 음식 재료 페이지
		페이지 resonse단계에서 json 형식의 자료를 브라우저로 전송할 겁니다. 이를 싫어하는 메뉴, 싫어하는 재료에서
		참조할 수 있도록 script를 수정하는 작업이 필요합니다.
		
	-나만을 위한 추전기능
		프로필 조회 후 사용자에게 맞는 메뉴 추천 리스트를 json 형태로 전달할 겁니다.
		이를 카드형태로 변환할 수 있는 template 코드를 작성해야합니다.
		
	
	-프론트 페이지 form 전달 방식
		form 전달 시에 에러가 많이 발생합니다.
		최대한 렌더링 요소를 배제하고 디자인 후 템플릿 문법을 적용해주세요
		form 을 만들었다면 form 태그 안에 {% csrf_token %} 을 넣으세요		
	
	* 프론트 페이지를 제작하는 사람들은 django 템플릿 문법을 익혀야 합니다.		
	* 각 페이지 기능별 회원가입, 로그인, 메인페이지, 마이페이지 단위로 html 파일, css 파일을 관리하세요
	* 모바일에서 환경에서 접속때 UI가 틀어지지 않도록 만들어주세요
	
프로필에 따른 음식 추천

	1. 크롤링 단계
		음식정보를 크롤링하여 정형 데이터로 만들어야함
		음식 : 재료 정보 수집
		네이버 음식백과 크롤러 만들기
		
			음식의 URL 파싱 완료, 해당 음식 URL에 맞는 규칙적용이 필요
				->각 음식백과의 자료별 크롤링 규칙을 상이하게 작성해야함을 확인
		
		최종 크롤링 결과를 Json 파일로 저장한 후 이를 DB로 마이그레이션 할 수있는 방안을 모색해야함
		
	2. 유사도 분석 단계
		각 사용자별 유사도 분석이 필요 프로필 을 Materix 형대로 핸들링 할 수 있도록 만들어야함
		사용할 유사도 공식 조사 및 적용
		- 우선 Content-based Filtering으로 진행/계정생성 후 Collaborative Filtering
		
	3. 회원과 유사한 회원 내림차순으로 뽑아내는 작업
	
	4. 유사한 회원이 좋아하는 음식 리스트를 만드는단계
	
	5. 싫어하는 재료, 음식이 들어가는 메뉴를 필터링 하는단계
	
	6. 클라이언트에게 전송
