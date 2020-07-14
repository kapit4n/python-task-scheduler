import { Component } from '@angular/core';
import { AuthService } from './shared/services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Task Manager';

  constructor(
    private authService: AuthService,
  ) {
  }

  get isAuthenticated(): boolean {
    return this.authService.checkAuthenticated();
  }

  logout() {
    this.authService.signOut();
  }

}
