# Python Mob Hunt Game

## 프로젝트 소개
Python 상속(Class Inheritance) 실습에서 만든 몬스터 클래스를 활용하여 만든 간단한 몹 잡기 게임입니다.

GitHub Branch, Pull Request, Issue를 이용한 협업과 Antigravity Coding Agent를 활용한 AI 협업 개발을 학습하기 위한 프로젝트입니다.

## 주요 기능

- 플레이어 생성
- 몬스터 공격
- 몬스터 HP 감소
- 몬스터 처치
- 터미널 메뉴 기반 게임 진행

## 프로젝트 구조

```text
python-mob-hunt-game/
├── main.py      # 프로그램 시작
├── monster.py   # 몬스터 클래스
├── player.py    # 플레이어 클래스
├── battle.py    # 전투 시스템
├── game.py      # 게임 화면
└── README.md
```

## 설치 방법

Python 3.10 이상이 설치되어 있어야 합니다.

```bash
git clone <repository-url>
cd python-mob-hunt-game
```

## 실행 방법

```bash
python main.py
```

실행 후 터미널에서 메뉴를 선택하여 게임을 진행합니다.

## 팀원 역할

| 팀원 | 담당 파일 |
|------|-----------|
| 팀원 A | player.py |
| 팀원 B | battle.py |
| 팀원 C | game.py, main.py |

## AI Agent 활용

- GitHub Issue를 작성하였다.
- Antigravity Coding Agent에게 Issue를 전달하였다.
- AI가 생성한 코드를 git diff로 검토하였다.
- Pull Request를 통해 사람이 최종 검토하였다.

## 향후 개선 사항

- 여러 종류의 몬스터 선택
- 아이템 시스템
- 경험치 시스템
- 레벨업
- pygame 기반 GUI
