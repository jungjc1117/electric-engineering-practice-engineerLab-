from PIL import Image
import os

def print_image_dimensions(folder_path):
    """
    지정된 폴더 내 모든 이미지 파일의 가로, 세로 길이를 출력하는 함수

    Args:
        folder_path (str): 이미지가 저장된 폴더의 경로
    """
    
    # 지원하는 이미지 파일 확장자 목록
    supported_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

    # 폴더가 존재하는지 확인
    if not os.path.isdir(folder_path):
        print(f"오류: '{folder_path}' 폴더를 찾을 수 없습니다.")
        return

    # 폴더 내 파일 목록을 순회
    for filename in os.listdir(folder_path):
        # 파일 확장자가 이미지인지 확인 (대소문자 무시)
        if filename.lower().endswith(supported_extensions):
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Pillow를 사용해 이미지 열기
                with Image.open(file_path) as img:
                    width, height = img.size
                    
                    # {가로}, {세로} 길이를 따로 출력
                    print(f"{width} {height}")
                    # print(f"가로: {width}px")
                    # print(f"세로: {height}px")
                    # print("-" * 20)  # 구분선
                    
            except Exception as e:
                print(f"오류: {filename} 파일을 여는 중 오류가 발생했습니다. ({e})")

# 사용 예시: 'images'라는 폴더에 이미지가 있다고 가정
image_folder = '6'  # 이 경로를 실제 이미지 폴더 경로로 변경하세요
print_image_dimensions(image_folder)